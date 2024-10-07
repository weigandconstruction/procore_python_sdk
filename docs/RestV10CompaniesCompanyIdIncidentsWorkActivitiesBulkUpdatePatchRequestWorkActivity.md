# RestV10CompaniesCompanyIdIncidentsWorkActivitiesBulkUpdatePatchRequestWorkActivity

IDs of all Work Activities specified for bulk update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**active** | **bool** | Flag that denotes if the Work Activities are available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_incidents_work_activities_bulk_update_patch_request_work_activity import RestV10CompaniesCompanyIdIncidentsWorkActivitiesBulkUpdatePatchRequestWorkActivity

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdIncidentsWorkActivitiesBulkUpdatePatchRequestWorkActivity from a JSON string
rest_v10_companies_company_id_incidents_work_activities_bulk_update_patch_request_work_activity_instance = RestV10CompaniesCompanyIdIncidentsWorkActivitiesBulkUpdatePatchRequestWorkActivity.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdIncidentsWorkActivitiesBulkUpdatePatchRequestWorkActivity.to_json())

# convert the object into a dict
rest_v10_companies_company_id_incidents_work_activities_bulk_update_patch_request_work_activity_dict = rest_v10_companies_company_id_incidents_work_activities_bulk_update_patch_request_work_activity_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdIncidentsWorkActivitiesBulkUpdatePatchRequestWorkActivity from a dict
rest_v10_companies_company_id_incidents_work_activities_bulk_update_patch_request_work_activity_from_dict = RestV10CompaniesCompanyIdIncidentsWorkActivitiesBulkUpdatePatchRequestWorkActivity.from_dict(rest_v10_companies_company_id_incidents_work_activities_bulk_update_patch_request_work_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


