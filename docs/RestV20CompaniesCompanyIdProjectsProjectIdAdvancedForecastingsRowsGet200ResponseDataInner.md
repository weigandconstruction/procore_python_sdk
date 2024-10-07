# RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInner

Advanced forecasting Row Summarized

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_line_item_id** | **str** | ID of the line item. | [optional] 
**wbs_code_id** | **str** | ID of the WBS code | [optional] 
**start_date** | **str** | The start date of the line item | [optional] 
**end_date** | **str** | The end date of the line item | [optional] 
**curve** | **str** | The curve of the line item. For more information about the curve distribution visit https://support.procore.com/faq/how-do-procores-advanced-forecasting-curves-distribute-projected-cost-to-complete-amounts | [optional] 
**forecast_to_complete** | **float** | The forecast to complete of the line item | [optional] 
**periods** | [**List[RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInnerPeriodsInner]**](RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInnerPeriodsInner.md) | The periods of the line item | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response_data_inner import RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInner from a JSON string
rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response_data_inner_instance = RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInner.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response_data_inner_dict = rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response_data_inner_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInner from a dict
rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response_data_inner_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200ResponseDataInner.from_dict(rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


