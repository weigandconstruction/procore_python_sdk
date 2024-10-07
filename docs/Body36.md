# Body36


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**project_role** | [**ProjectRole**](ProjectRole.md) |  | 

## Example

```python
from procore_sdk.models.body36 import Body36

# TODO update the JSON string below
json = "{}"
# create an instance of Body36 from a JSON string
body36_instance = Body36.from_json(json)
# print the JSON string representation of the object
print(Body36.to_json())

# convert the object into a dict
body36_dict = body36_instance.to_dict()
# create an instance of Body36 from a dict
body36_from_dict = Body36.from_dict(body36_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


