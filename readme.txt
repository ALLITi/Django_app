My Django Tree Menu App

This is a Django app that implements a tree menu with the following features:
- The menu is implemented using a custom template tag
- Only the branch above the selected item is expanded
- The first level of the branch below the selected item is also expanded
- The menu is stored in a database
- The menu can be edited using the Django admin interface
- The active menu item is determined by the URL of the current page
- Multiple menus can be displayed on a single page
- Clicking on a menu item navigates to the specified URL, which can be either explicit or named
- The menu is rendered with a single database query

Installation

1. Clone the repository
2. Install the dependencies with pip install -r requirements.txt
3. Run the development server with python manage.py runserver

Usage

1. Add menu items using the Django admin interface
2. In your template, use the template tag {% draw_menu 'main_menu' %} to draw the menu with the name 'main_menu'

License

This project is licensed under the MIT License.
