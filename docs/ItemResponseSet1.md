# ItemResponseSet1

Item Response Set object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Response Set | [optional] 
**active** | **bool** | Indicates whether a Response Set is available for use | [optional] 

## Example

```python
from procore_sdk.models.item_response_set1 import ItemResponseSet1

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResponseSet1 from a JSON string
item_response_set1_instance = ItemResponseSet1.from_json(json)
# print the JSON string representation of the object
print(ItemResponseSet1.to_json())

# convert the object into a dict
item_response_set1_dict = item_response_set1_instance.to_dict()
# create an instance of ItemResponseSet1 from a dict
item_response_set1_from_dict = ItemResponseSet1.from_dict(item_response_set1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


