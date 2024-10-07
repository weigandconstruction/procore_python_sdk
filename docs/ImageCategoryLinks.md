# ImageCategoryLinks

Action links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show** | **str** | Link to show images in category | [optional] 
**delete** | **str** | Link to delete the category | [optional] 
**update** | **str** | Link to update the category | [optional] 

## Example

```python
from procore_sdk.models.image_category_links import ImageCategoryLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCategoryLinks from a JSON string
image_category_links_instance = ImageCategoryLinks.from_json(json)
# print the JSON string representation of the object
print(ImageCategoryLinks.to_json())

# convert the object into a dict
image_category_links_dict = image_category_links_instance.to_dict()
# create an instance of ImageCategoryLinks from a dict
image_category_links_from_dict = ImageCategoryLinks.from_dict(image_category_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


