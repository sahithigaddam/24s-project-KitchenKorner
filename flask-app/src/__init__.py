# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_root_password.txt').readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'KitchenKorner'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 boilerplate app</h1>"

    # Import the various Beluprint Objects
    from src.Comments.Comments import comments
    from src.Cookbook.Cookbook import cookbook
    from src.Direct_Messages.Direct_Messages import direct_messages
    from src.External_Messages.External_Messages import external_messages
    from src.Feeds.Feeds import feeds
    from src.Filters.Filters import filters
    from src.Follows.Follows import follows
    from src.Ingredient_Details.Ingredient_Details import ingredient_details
    from src.Ingredients.Ingredients import ingredients
    from src.Posts.Posts import posts
    from src.Ratings.Ratings import ratings
    from src.Recipes.Recipes import recipes
    from src.Search.Search import search
    from src.Tags.Tags import tags
    from src.Users.Users import users


    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(comments,    url_prefix='/c')
    app.register_blueprint(cookbook,    url_prefix='/c')
    app.register_blueprint(direct_messages,    url_prefix='/d')
    app.register_blueprint(external_messages,    url_prefix='/e')
    app.register_blueprint(feeds,    url_prefix='/f')
    app.register_blueprint(filters,    url_prefix='/f')
    app.register_blueprint(follows,    url_prefix='/f')
    app.register_blueprint(ingredient_details,    url_prefix='/i')
    app.register_blueprint(ingredients,    url_prefix='/i')
    app.register_blueprint(posts,    url_prefix='/p')
    app.register_blueprint(ratings,    url_prefix='/r')
    app.register_blueprint(recipes,    url_prefix='/r')
    app.register_blueprint(search,    url_prefix='/s')
    app.register_blueprint(tags,    url_prefix='/t')
    app.register_blueprint(users,    url_prefix='/u')



    # Don't forget to return the app object
    return app