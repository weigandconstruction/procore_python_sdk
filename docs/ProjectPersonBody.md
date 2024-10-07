# ProjectPersonBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**ProjectPerson**](ProjectPerson.md) |  | 

## Example

```python
from procore_sdk.models.project_person_body import ProjectPersonBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPersonBody from a JSON string
project_person_body_instance = ProjectPersonBody.from_json(json)
# print the JSON string representation of the object
print(ProjectPersonBody.to_json())

# convert the object into a dict
project_person_body_dict = project_person_body_instance.to_dict()
# create an instance of ProjectPersonBody from a dict
project_person_body_from_dict = ProjectPersonBody.from_dict(project_person_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


