# Body106


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**updates** | [**List[Body104CoordinationIssue]**](Body104CoordinationIssue.md) | An array of coordination issue payloads | 

## Example

```python
from procore_sdk.models.body106 import Body106

# TODO update the JSON string below
json = "{}"
# create an instance of Body106 from a JSON string
body106_instance = Body106.from_json(json)
# print the JSON string representation of the object
print(Body106.to_json())

# convert the object into a dict
body106_dict = body106_instance.to_dict()
# create an instance of Body106 from a dict
body106_from_dict = Body106.from_dict(body106_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


