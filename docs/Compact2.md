# Compact2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**name** | **str** | The name of the Project | [optional] 

## Example

```python
from procore_sdk.models.compact2 import Compact2

# TODO update the JSON string below
json = "{}"
# create an instance of Compact2 from a JSON string
compact2_instance = Compact2.from_json(json)
# print the JSON string representation of the object
print(Compact2.to_json())

# convert the object into a dict
compact2_dict = compact2_instance.to_dict()
# create an instance of Compact2 from a dict
compact2_from_dict = Compact2.from_dict(compact2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


