# Location7


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
from procore_sdk.models.location7 import Location7

# TODO update the JSON string below
json = "{}"
# create an instance of Location7 from a JSON string
location7_instance = Location7.from_json(json)
# print the JSON string representation of the object
print(Location7.to_json())

# convert the object into a dict
location7_dict = location7_instance.to_dict()
# create an instance of Location7 from a dict
location7_from_dict = Location7.from_dict(location7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


