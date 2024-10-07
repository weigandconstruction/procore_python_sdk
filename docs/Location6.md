# Location6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Location ID | [optional] 
**name** | **str** | Location name | [optional] 
**node_name** | **str** | Location node name | [optional] 
**parent_id** | **int** | Location parent id | [optional] 
**created_at** | **datetime** | Timestamp of Location creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Location | [optional] 

## Example

```python
from procore_sdk.models.location6 import Location6

# TODO update the JSON string below
json = "{}"
# create an instance of Location6 from a JSON string
location6_instance = Location6.from_json(json)
# print the JSON string representation of the object
print(Location6.to_json())

# convert the object into a dict
location6_dict = location6_instance.to_dict()
# create an instance of Location6 from a dict
location6_from_dict = Location6.from_dict(location6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


