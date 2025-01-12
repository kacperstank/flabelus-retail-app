from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.utils.timezone import now
from ..models import Store
from catalog.serializers.login import UserLoginSerializer, StoreSerializer


class LoginView(APIView):
    """
    API view to handle user login.

    This view authenticates a user based on the provided username and password.
    If the credentials are valid, it updates the user's last login timestamp,
    retrieves their associated user information, and lists the stores they are linked to.

    """

    def post(self, request):
        """
        Handle POST requests to authenticate a user.

        Args:
            request: The HTTP request object containing username and password in the body.

        Returns:
            Response: A JSON object with user data and associated stores if authentication succeeds,
                      or an error message if authentication fails.

        # TODO: Add rate limiting
        """
        # Log received data
        print("Hey")
        print(f"Received request data: {request.data}")

        # Extract username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Log the extracted values
        print(f"Extracted username: {username}, password: {password}")

        # Validate that both username and password are provided
        if not username or not password:
            return Response(
                {'error': 'Username and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Attempt to authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            # Update the last login timestamp for the authenticated user
            user.last_login = now()
            user.save()

            # Serialize the authenticated user's data
            user_data = UserLoginSerializer(user).data

            # Retrieve stores associated with the authenticated user
            stores = Store.objects.filter(userstore__user=user)
            store_data = StoreSerializer(stores, many=True).data

            # Return the user data and associated stores
            return Response(
                {
                    'user': user_data,
                    'stores': store_data,
                },
                status=status.HTTP_200_OK
            )
        else:
            # Authentication failed
            return Response(
                {'error': 'Invalid username or password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )