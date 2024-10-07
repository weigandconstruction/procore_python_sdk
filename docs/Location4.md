# Location4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_name** | **str** | The Node Name of the Location | [optional] 
**parent_id** | **int** | The ID of the Parent Location of the Location | [optional] 

## Example

```python
from procore_sdk.models.location4 import Location4

# TODO update the JSON string below
json = "{}"
# create an instance of Location4 from a JSON string
location4_instance = Location4.from_json(json)
# print the JSON string representation of the object
print(Location4.to_json())

# convert the object into a dict
location4_dict = location4_instance.to_dict()
# create an instance of Location4 from a dict
location4_from_dict = Location4.from_dict(location4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


