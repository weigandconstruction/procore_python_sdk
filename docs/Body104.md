# Body104


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**coordination_issue** | [**Body104CoordinationIssue**](Body104CoordinationIssue.md) |  | 

## Example

```python
from procore_sdk.models.body104 import Body104

# TODO update the JSON string below
json = "{}"
# create an instance of Body104 from a JSON string
body104_instance = Body104.from_json(json)
# print the JSON string representation of the object
print(Body104.to_json())

# convert the object into a dict
body104_dict = body104_instance.to_dict()
# create an instance of Body104 from a dict
body104_from_dict = Body104.from_dict(body104_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


