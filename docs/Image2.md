# Image2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | **bool** | The Private status of the Image. Defaults to a project configuration. | [optional] 
**description** | **str** | Image description | [optional] 
**image_category_id** | **int** | Image Category ID to move the Image to | [optional] 
**location_id** | **int** | If you want to use an existing location and you have the ID of that existing location use this. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**trade_ids** | **List[int]** | An array of IDs of the Trades of the Image | [optional] 
**log_date** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.image2 import Image2

# TODO update the JSON string below
json = "{}"
# create an instance of Image2 from a JSON string
image2_instance = Image2.from_json(json)
# print the JSON string representation of the object
print(Image2.to_json())

# convert the object into a dict
image2_dict = image2_instance.to_dict()
# create an instance of Image2 from a dict
image2_from_dict = Image2.from_dict(image2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


