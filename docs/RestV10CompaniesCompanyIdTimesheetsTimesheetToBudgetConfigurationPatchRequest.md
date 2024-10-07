# RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_to_existing** | **bool** | Whether the passed in Line Item Type ID should be applied to existing timecard entries (erp or not) | [optional] 
**line_item_type_id** | **int** | Line Item Type ID | 
**erp_default_line_item_type_id** | **int** | ERP Line Item Type ID | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request import RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest from a JSON string
rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request_instance = RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request_dict = rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest from a dict
rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request_from_dict = RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest.from_dict(rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


