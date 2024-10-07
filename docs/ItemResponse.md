# ItemResponse

Item Response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Item Status - Value for Default-Typed items. Allowed values are &#39;conforming&#39;, &#39;non_conforming&#39;, and &#39;not_applicable&#39;. | [optional] 
**response_option_id** | **int** | Response Option ID - Value for Multiple Choice Response Items | [optional] 
**text_value** | **str** | Text Response - Value for Open Ended Text Items | [optional] 
**number_value** | **int** | Number Response - Value for Open Ended Number Items | [optional] 
**date_value** | **date** | Date Response - Value for Open Ended Date Items. Format should be YYYY-MM-DD | [optional] 

## Example

```python
from procore_sdk.models.item_response import ItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResponse from a JSON string
item_response_instance = ItemResponse.from_json(json)
# print the JSON string representation of the object
print(ItemResponse.to_json())

# convert the object into a dict
item_response_dict = item_response_instance.to_dict()
# create an instance of ItemResponse from a dict
item_response_from_dict = ItemResponse.from_dict(item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


