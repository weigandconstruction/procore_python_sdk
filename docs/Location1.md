# Location1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Location ID | [optional] 
**name** | **str** | Location name | [optional] 
**node_name** | **str** | Location node name | [optional] 
**parent_id** | **int** | Location parent id | [optional] 
**created_at** | **datetime** | Timestamp of Location creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Location | [optional] 
**code** | **str** | The unique code for this Location | [optional] 

## Example

```python
from procore_sdk.models.location1 import Location1

# TODO update the JSON string below
json = "{}"
# create an instance of Location1 from a JSON string
location1_instance = Location1.from_json(json)
# print the JSON string representation of the object
print(Location1.to_json())

# convert the object into a dict
location1_dict = location1_instance.to_dict()
# create an instance of Location1 from a dict
location1_from_dict = Location1.from_dict(location1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


