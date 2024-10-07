# ImageCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Image Category ID | [optional] 
**count** | **int** | Amount of images in category | [optional] 
**cover_photo** | **str** | Cover photo url | [optional] 
**created_at** | **datetime** | Image Category created at | [optional] 
**links** | [**ImageCategoryLinks**](ImageCategoryLinks.md) |  | [optional] 
**name** | **str** | Image Category name | [optional] 
**private** | **bool** | Private status | [optional] 
**updated_at** | **datetime** | Image Category updated at | [optional] 
**position** | **int** | Image Category Position | [optional] 

## Example

```python
from procore_sdk.models.image_category import ImageCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCategory from a JSON string
image_category_instance = ImageCategory.from_json(json)
# print the JSON string representation of the object
print(ImageCategory.to_json())

# convert the object into a dict
image_category_dict = image_category_instance.to_dict()
# create an instance of ImageCategory from a dict
image_category_from_dict = ImageCategory.from_dict(image_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


