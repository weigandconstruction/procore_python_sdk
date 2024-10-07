# Location8


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Location ID | [optional] 
**name** | **str** | Location name | [optional] 
**code** | **str** | Location code | [optional] 
**node_name** | **str** | Location node name | [optional] 
**parent_id** | **int** | Location parent id | [optional] 
**created_at** | **datetime** | Timestamp of Location creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Location | [optional] 

## Example

```python
from procore_sdk.models.location8 import Location8

# TODO update the JSON string below
json = "{}"
# create an instance of Location8 from a JSON string
location8_instance = Location8.from_json(json)
# print the JSON string representation of the object
print(Location8.to_json())

# convert the object into a dict
location8_dict = location8_instance.to_dict()
# create an instance of Location8 from a dict
location8_from_dict = Location8.from_dict(location8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


