from django.db import models

class Role(models.Model):
    """
    Stores all possible user roles.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=50, unique=True)  # Unique role name (e.g., 'Clerk')
    description = models.TextField(blank=True, null=True)  # Optional role description

    class Meta:
        db_table = "roles"  # Explicit table name to match SQL schema
        verbose_name_plural = "Roles"  # Display name in admin interface

    def __str__(self):
        return self.name

class User(models.Model):
    """
    Stores system users, including login credentials and roles.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    username = models.CharField(max_length=50, unique=True)  # Unique login username
    password = models.CharField(max_length=255)  # Encrypted user password
    role = models.ForeignKey(
        Role, on_delete=models.RESTRICT, db_column="role_id"
    )  # Links to the Role model
    email = models.EmailField(max_length=100, blank=True, unique=True, null=True)  # Optional user email
    first_name = models.CharField(max_length=50, blank=True, null=True)  # First name of the user
    last_name = models.CharField(max_length=50, blank=True, null=True)  # Last name of the user
    profile_picture = models.TextField(blank=True, null=True)  # Optional profile picture URL
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    last_login = models.DateTimeField(blank=True, null=True)  # Last login timestamp

    class Meta:
        db_table = "users"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["role"], name="idx_users_role_id"),  # Index on role_id
        ]
        verbose_name_plural = "Users"  # Display name in admin interface

    def __str__(self):
        return self.username


class Region(models.Model):
    """
    Stores information about geographic regions, including their name and
    assigned regional manager.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100, unique=True)  # Unique name of the region
    regional_manager = models.ForeignKey(
        "User", on_delete=models.SET_NULL, null=True, blank=True, db_column="regional_manager_id"
    )  # Reference to the User model as regional manager; sets to NULL if deleted
    notes = models.TextField(blank=True, null=True)  # Optional additional notes about the region
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the region was created

    class Meta:
        db_table = "regions"  # Ensures the table is named `regions` in the database
        indexes = [
            models.Index(fields=["regional_manager"], name="idx_regional_manager_id"),  # Index on regional_manager_id
        ]
        verbose_name_plural = "Regions"  # Display name in admin interface

    def __str__(self):
        return self.name

class Store(models.Model):
    """
    Stores information about individual stores, including location,
    contact details, and associated region.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)  # Name of the store
    location = models.TextField()  # Physical address or location of the store
    email = models.EmailField(max_length=100, blank=True, null=True)  # Optional contact email
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Optional contact phone number
    manager = models.ForeignKey(
        "User", on_delete=models.SET_NULL, blank=True, null=True, db_column="manager_id"
    )  # Reference to the user managing this store, allows NULL on deletion
    region = models.ForeignKey(
        "Region", on_delete=models.RESTRICT, db_column="region_id"
    )  # Reference to the region, restricted deletion

    class Meta:
        db_table = "stores"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["region"], name="idx_stores_region_id"),  # Index on region_id
            models.Index(fields=["manager"], name="idx_stores_manager_id"),  # Index on manager_id
        ]
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name


class UserStore(models.Model):
    """
    Creates a many-to-many relationship between users and stores.
    Links which users work at which stores.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, db_column="user_id"
    )  # Reference to a user, cascade deletion
    store = models.ForeignKey(
        "Store", on_delete=models.RESTRICT, db_column="store_id"
    )  # Reference to a store, restricted deletion

    class Meta:
        db_table = "user_stores"  # Explicit table name to match SQL schema
        unique_together = (("user", "store"),)  # Enforces unique combinations of user and store
        verbose_name_plural = "User Stores"

    def __str__(self):
        return f"{self.user.username} - {self.store.name}"


class Category(models.Model):
    """
    Stores product categories (e.g., shoes, earrings, coats).
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=50, unique=True)  # Unique name of the category (e.g., 'Shoes')
    description = models.TextField(blank=True, null=True)  # Optional detailed description
    parent = models.ForeignKey(
        "self", on_delete=models.RESTRICT, blank=True, null=True, db_column="parent_id"
    )  # Reference to the parent category
    icon_url = models.TextField(blank=True, null=True)  # Optional URL or path to an image/icon
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp on creation

    class Meta:
        db_table = "categories"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["parent"], name="idx_categories_parent_id"),  # Index on parent_id
        ]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Stores general information about all products, regardless of type (e.g., shoes, earrings, coats).
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)  # Name of the product
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, blank=True, null=True, db_column="category_id"
    )  # Reference to the category
    description = models.TextField(blank=True, null=True)  # General description
    image = models.TextField(blank=True, null=True)  # Optional path or URL to the product's main image
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp on creation

    class Meta:
        db_table = "products"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["name"], name="idx_products_name"),  # Index for name-based lookups
            models.Index(fields=["category"], name="idx_products_category_id"),  # Index for category lookups
            models.Index(fields=["price"], name="idx_products_price"),  # Index for price lookups
            models.Index(fields=["created_at"], name="idx_products_created_at"),  # Index for time-based queries
        ]
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class ShoeDetail(models.Model):
    """
    Stores specific information for shoes, linked to the general Product table.
    """
    product = models.OneToOneField(
        "Product", on_delete=models.CASCADE, primary_key=True, db_column="product_id"
    )  # Links to the product ID
    color = models.CharField(max_length=50)  # Specific color of the shoe
    materials = models.TextField(blank=True, null=True)  # Optional materials used in the shoe's construction

    class Meta:
        db_table = "shoe_details"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["color"], name="idx_shoe_details_color"),  # Index on color
        ]
        verbose_name_plural = "Shoe Details"

    def __str__(self):
        return f"Shoe Detail for Product ID {self.product.id}"

class EarringDetail(models.Model):
    """
    Stores specific information for earrings, linked to the general Product table.
    """
    product = models.OneToOneField(
        "Product", on_delete=models.CASCADE, primary_key=True, db_column="product_id"
    )  # Links to the product ID
    material = models.CharField(max_length=100)  # Material of the earrings (e.g., gold, silver)
    style = models.CharField(max_length=100, blank=True, null=True)  # Optional style of the earrings (e.g., hoop, stud)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Optional weight in grams

    class Meta:
        db_table = "earring_details"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["material"], name="idx_earring_details_material"),  # Index on material
        ]
        verbose_name_plural = "Earring Details"

    def __str__(self):
        return f"Earring Detail for Product ID {self.product.id}"

class ShoeStock(models.Model):
    """
    Manages stock and sizes for shoes at specific stores.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for stock tracking
    sku = models.CharField(max_length=50, unique=True)  # Unique Stock Keeping Unit for tracking
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, db_column="product_id"
    )  # Links to the shoe's product ID
    store = models.ForeignKey(
        "Store", on_delete=models.RESTRICT, db_column="store_id"
    )  # Links to the store stocking the shoe
    size = models.DecimalField(max_digits=3, decimal_places=1)  # Shoe size (e.g., 36, 36.5)
    stock = models.IntegerField(default=0)  # Quantity of this size in stock

    class Meta:
        db_table = "shoe_stock"  # Explicit table name to match SQL schema
        constraints = [
            models.UniqueConstraint(
                fields=["product", "store", "size"], name="unique_shoe_stock"
            )  # Prevents duplicate entries for the same size at the same store
        ]
        indexes = [
            models.Index(fields=["product"], name="idx_shoe_stock_product_id"),
            models.Index(fields=["store"], name="idx_shoe_stock_store_id"),
            models.Index(fields=["size"], name="idx_shoe_stock_size"),
            models.Index(fields=["store", "product"], name="idx_shoe_stock_store_product"),
        ]
        verbose_name_plural = "Shoe Stock"

    def __str__(self):
        return f"Shoe Stock SKU: {self.sku}"

class EarringStock(models.Model):
    """
    Manages stock for earrings at specific stores.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for stock tracking
    sku = models.CharField(max_length=50, unique=True)  # Unique Stock Keeping Unit for tracking
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, db_column="product_id"
    )  # Links to the earring product ID
    store = models.ForeignKey(
        "Store", on_delete=models.RESTRICT, db_column="store_id"
    )  # Links to the store stocking the earrings
    stock = models.IntegerField(default=0)  # Quantity of this item in stock

    class Meta:
        db_table = "earring_stock"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["product"], name="idx_earring_stock_product_id"),
            models.Index(fields=["store"], name="idx_earring_stock_store_id"),
        ]
        verbose_name_plural = "Earring Stock"

    def __str__(self):
        return f"Earring Stock SKU: {self.sku}"


class Tag(models.Model):
    """
    Stores the list of all possible tags that can be associated with products.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for tag identification
    name = models.CharField(max_length=50, unique=True)  # Unique tag name (e.g., "Red", "Summer Collection 2024")
    description = models.TextField(blank=True, null=True)  # Optional description for the tag
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically records when the tag is created

    class Meta:
        db_table = "tags"  # Explicit table name to match SQL schema
        verbose_name_plural = "Tags"  # Display name for admin interface

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    """
    Creates a many-to-many relationship between products and tags.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for relationship tracking
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, db_column="product_id"
    )  # Reference to the product
    tag = models.ForeignKey(
        "Tag", on_delete=models.CASCADE, db_column="tag_id"
    )  # Reference to the tag

    class Meta:
        db_table = "product_tags"  # Explicit table name to match SQL schema
        indexes = [
            models.Index(fields=["product"], name="idx_product_tags_product_id"),
            models.Index(fields=["tag"], name="idx_product_tags_tag_id"),
        ]
        verbose_name_plural = "Product Tags"  # Display name for admin interface

    def __str__(self):
        return f"{self.product.name} - {self.tag.name}"


class Sale(models.Model):
    """
    Tracks individual sales transactions made by users.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for sale identification
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, db_column="user_id"
    )  # Reference to the user (clerk) who made the sale
    store = models.ForeignKey(
        "Store", on_delete=models.RESTRICT, db_column="store_id"
    )  # Reference to the store where the sale occurred
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the sale
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the sale was created

    class Meta:
        db_table = "sales"  # Explicitly name the table in the database
        indexes = [
            models.Index(fields=["user"], name="idx_sales_user_id"),  # Index on user_id
            models.Index(fields=["store"], name="idx_sales_store_id"),  # Index on store_id
        ]
        verbose_name_plural = "Sales"  # Display name in admin interface

    def __str__(self):
        return f"Sale {self.id} by User {self.user_id}"

class SaleItem(models.Model):
    """
    Tracks individual items sold within a sale.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for sale item identification
    sale = models.ForeignKey(
        "Sale", on_delete=models.CASCADE, db_column="sale_id"
    )  # Reference to the sale this item belongs to
    product = models.ForeignKey(
        "Product", on_delete=models.RESTRICT, db_column="product_id"
    )  # Reference to the product being sold
    size = models.DecimalField(max_digits=3, decimal_places=1)  # Size of the product sold (e.g., 36.5)
    quantity = models.PositiveIntegerField()  # Number of units sold (must be > 0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit of the product
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False
    )  # Total price, calculated automatically

    class Meta:
        db_table = "sale_items"  # Explicitly name the table in the database
        indexes = [
            models.Index(fields=["sale"], name="idx_sale_items_sale_id"),  # Index on sale_id
            models.Index(fields=["product"], name="idx_sale_items_product_id"),  # Index on product_id
        ]
        verbose_name_plural = "Sale Items"  # Display name in admin interface

    def save(self, *args, **kwargs):
        # Automatically calculate total_price before saving
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item {self.id} of Sale {self.sale_id}"