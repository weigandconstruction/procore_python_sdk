# RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of record | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**man_hours** | **str** | Total man hours (num_workers x num_hours) | [optional] 
**notes** | **str** | Additional notes | [optional] 
**num_workers** | **int** | Number of workers | [optional] 
**num_hours** | **str** | Number of hours for each worker | [optional] 
**position** | **int** | Position in which this entry was recorded for the day | [optional] 
**status** | **str** | Is a log pending or approved | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor** | [**RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor.md) |  | [optional] 
**user** | [**RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerUser**](RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerUser.md) |  | [optional] 
**contact** | [**RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact**](RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact.md) |  | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location2**](Location2.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**permissions** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_manpower_logs_get200_response_inner_instance = RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_manpower_logs_get200_response_inner_dict = rest_v10_projects_project_id_manpower_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_manpower_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_manpower_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


