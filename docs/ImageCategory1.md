# ImageCategory1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Image Category | 
**private** | **bool** | The Private status of the Image Category | [optional] [default to False]
**album_cover_id** | **int** | ID of an Image that is the cover Image of the Image Category. | [optional] 

## Example

```python
from procore_sdk.models.image_category1 import ImageCategory1

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCategory1 from a JSON string
image_category1_instance = ImageCategory1.from_json(json)
# print the JSON string representation of the object
print(ImageCategory1.to_json())

# convert the object into a dict
image_category1_dict = image_category1_instance.to_dict()
# create an instance of ImageCategory1 from a dict
image_category1_from_dict = ImageCategory1.from_dict(image_category1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


