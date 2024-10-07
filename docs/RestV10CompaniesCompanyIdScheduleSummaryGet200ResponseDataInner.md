# RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Datetime at beginning of day | [optional] 
**projects_count** | **int** | Number of projects with tasks or calendar items on this day | [optional] 
**projects** | [**List[RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner]**](RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInnerProjectsInner.md) | List of projects with counts of tasks or calendar items on this day. The size of this list is limited by the &#x60;limit_per_day&#x60; query parameter. The order of this list is determined by the &#x60;sort_key&#x60; and &#x60;sort_dir&#x60; query parameters. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_schedule_summary_get200_response_data_inner import RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner from a JSON string
rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_instance = RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_dict = rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner from a dict
rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_from_dict = RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner.from_dict(rest_v10_companies_company_id_schedule_summary_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


