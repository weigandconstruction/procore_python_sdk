# Party1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Timecard entry id | [optional] 
**name** | **str** | Party Name | [optional] 

## Example

```python
from procore_sdk.models.party1 import Party1

# TODO update the JSON string below
json = "{}"
# create an instance of Party1 from a JSON string
party1_instance = Party1.from_json(json)
# print the JSON string representation of the object
print(Party1.to_json())

# convert the object into a dict
party1_dict = party1_instance.to_dict()
# create an instance of Party1 from a dict
party1_from_dict = Party1.from_dict(party1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


