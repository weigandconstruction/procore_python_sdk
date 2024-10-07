# ProjectCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the company. | [optional] 
**name** | **str** | The Company name | [optional] 

## Example

```python
from procore_sdk.models.project_company import ProjectCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCompany from a JSON string
project_company_instance = ProjectCompany.from_json(json)
# print the JSON string representation of the object
print(ProjectCompany.to_json())

# convert the object into a dict
project_company_dict = project_company_instance.to_dict()
# create an instance of ProjectCompany from a dict
project_company_from_dict = ProjectCompany.from_dict(project_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


