# TimesheetToBudgetConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | TimesheetToBudgetConfiguration ID | [optional] 
**line_item_type_id** | **int** | Line Item Type ID (Cost Type) | [optional] 
**erp_default_line_item_type_id** | **int** | ERP Line Item Type ID (Cost Type). Company must also be ERP integrated | [optional] 
**company_id** | **int** | Company ID | [optional] 
**has_backfilled** | **bool** | Whether the default Line Item Type ID has been backfilled to Timecard Entries | [optional] 

## Example

```python
from procore_sdk.models.timesheet_to_budget_configuration import TimesheetToBudgetConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetToBudgetConfiguration from a JSON string
timesheet_to_budget_configuration_instance = TimesheetToBudgetConfiguration.from_json(json)
# print the JSON string representation of the object
print(TimesheetToBudgetConfiguration.to_json())

# convert the object into a dict
timesheet_to_budget_configuration_dict = timesheet_to_budget_configuration_instance.to_dict()
# create an instance of TimesheetToBudgetConfiguration from a dict
timesheet_to_budget_configuration_from_dict = TimesheetToBudgetConfiguration.from_dict(timesheet_to_budget_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


