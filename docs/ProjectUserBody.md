# ProjectUserBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**ProjectUser**](ProjectUser.md) |  | 

## Example

```python
from procore_sdk.models.project_user_body import ProjectUserBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUserBody from a JSON string
project_user_body_instance = ProjectUserBody.from_json(json)
# print the JSON string representation of the object
print(ProjectUserBody.to_json())

# convert the object into a dict
project_user_body_dict = project_user_body_instance.to_dict()
# create an instance of ProjectUserBody from a dict
project_user_body_from_dict = ProjectUserBody.from_dict(project_user_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


