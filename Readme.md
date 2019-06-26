# Datascience 2 PPTX

Use this library to programatically create Powerpoint (PPTX) presentations from matplotlib and pandas objects.

The general workflow is:

1. Create a PPTX template (sorry, MS-Office seems to mandatory for this)
This template should have a set of slide layouts, each of which contains a set of placeholders

2. Generate your matplotlib ```Figure``` objects and your pandas ```dataframe```objects acording to your needs.

3. Generate a set of slides, each of which is a python dictionary such as:
        ``` 
           {
            "name": "Slide3",
            "layout": "LayoutName",
            'placeholders': {
                "Image Place Holder": matplotlib_figure_object
            }
            ```
            
4. Create a slideshow object using the path to the template ```slds = Slideshow(template=templatepath)```
5. Call a ```Execute``` method to compile the slideshow
6. Call the ```SaveTo``` method to save to a pptx file

In any case, check the tests for examples.
