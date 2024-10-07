# RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature

Company signature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**signature_text** | **str** | Acknowedgement text the signature was signed against. | [optional] 
**file_name** | **str** | File Name | [optional] 
**url** | **str** | URL | [optional] 
**medium_thumbnail_url** | **str** | URL | [optional] 
**large_thumbnail_url** | **str** | URL | [optional] 
**created_at** | **datetime** | Created at date | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_company_signature import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature from a JSON string
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_company_signature_instance = RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_company_signature_dict = rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_company_signature_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature from a dict
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_company_signature_from_dict = RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature.from_dict(rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_company_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


