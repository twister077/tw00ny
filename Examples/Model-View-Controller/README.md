## Model-View-Controller example

In this folder a MVC configuration example is show. In this way Models, Views and the Controllers are each neatly organized in their own separate python/html file. 

To enable a MVC based configuration do the following:
* Replace pyramid_example.py in the root of your project with the one in this folder. You can also just add `config.scan(package='controller')` to pyramid_example.py file under `if __name__ == '__main__'`.
* Copy the files models.py and controller.py to the root of your project

