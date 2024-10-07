# RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner

Project with counts. `tasks_count` is only present if its value is greater than 0. `calendar_items_count` is only present if its value is greater than 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project ID | [optional] 
**name** | **str** | Project Name | [optional] 
**tasks_count** | **int** | Number of tasks on this day | [optional] 
**calendar_items_count** | **int** | Number of calendar items on this day | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_projects_inner import RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner from a JSON string
rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_projects_inner_instance = RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_projects_inner_dict = rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_projects_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner from a dict
rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_projects_inner_from_dict = RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner.from_dict(rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


