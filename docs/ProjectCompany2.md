# ProjectCompany2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project Company | [optional] 
**name** | **str** | The name for the Project Company | [optional] 

## Example

```python
from procore_sdk.models.project_company2 import ProjectCompany2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCompany2 from a JSON string
project_company2_instance = ProjectCompany2.from_json(json)
# print the JSON string representation of the object
print(ProjectCompany2.to_json())

# convert the object into a dict
project_company2_dict = project_company2_instance.to_dict()
# create an instance of ProjectCompany2 from a dict
project_company2_from_dict = ProjectCompany2.from_dict(project_company2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


