# Body137


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_level** | [**BIMLevel**](BIMLevel.md) |  | 

## Example

```python
from procore_sdk.models.body137 import Body137

# TODO update the JSON string below
json = "{}"
# create an instance of Body137 from a JSON string
body137_instance = Body137.from_json(json)
# print the JSON string representation of the object
print(Body137.to_json())

# convert the object into a dict
body137_dict = body137_instance.to_dict()
# create an instance of Body137 from a dict
body137_from_dict = Body137.from_dict(body137_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


