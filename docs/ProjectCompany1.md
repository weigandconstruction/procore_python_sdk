# ProjectCompany1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company ID | [optional] 
**name** | **str** | Company name | [optional] 

## Example

```python
from procore_sdk.models.project_company1 import ProjectCompany1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCompany1 from a JSON string
project_company1_instance = ProjectCompany1.from_json(json)
# print the JSON string representation of the object
print(ProjectCompany1.to_json())

# convert the object into a dict
project_company1_dict = project_company1_instance.to_dict()
# create an instance of ProjectCompany1 from a dict
project_company1_from_dict = ProjectCompany1.from_dict(project_company1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


