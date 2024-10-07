# Body105


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**coordination_issue** | [**CoordinationIssue**](CoordinationIssue.md) |  | 

## Example

```python
from procore_sdk.models.body105 import Body105

# TODO update the JSON string below
json = "{}"
# create an instance of Body105 from a JSON string
body105_instance = Body105.from_json(json)
# print the JSON string representation of the object
print(Body105.to_json())

# convert the object into a dict
body105_dict = body105_instance.to_dict()
# create an instance of Body105 from a dict
body105_from_dict = Body105.from_dict(body105_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


