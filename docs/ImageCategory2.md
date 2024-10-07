# ImageCategory2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Image Category ID | [optional] 
**name** | **str** | Image Category name | [optional] 
**position** | **int** | Image Category position | [optional] 
**album_cover_id** | **int** | Album cover ID | [optional] 
**created_at** | **datetime** | Image Category created at | [optional] 
**private** | **bool** | Private status | [optional] 
**count** | **int** | Amount of images in category | [optional] 

## Example

```python
from procore_sdk.models.image_category2 import ImageCategory2

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCategory2 from a JSON string
image_category2_instance = ImageCategory2.from_json(json)
# print the JSON string representation of the object
print(ImageCategory2.to_json())

# convert the object into a dict
image_category2_dict = image_category2_instance.to_dict()
# create an instance of ImageCategory2 from a dict
image_category2_from_dict = ImageCategory2.from_dict(image_category2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


