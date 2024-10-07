# Body141


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_file** | [**BIMFile1**](BIMFile1.md) |  | 

## Example

```python
from procore_sdk.models.body141 import Body141

# TODO update the JSON string below
json = "{}"
# create an instance of Body141 from a JSON string
body141_instance = Body141.from_json(json)
# print the JSON string representation of the object
print(Body141.to_json())

# convert the object into a dict
body141_dict = body141_instance.to_dict()
# create an instance of Body141 from a dict
body141_from_dict = Body141.from_dict(body141_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


