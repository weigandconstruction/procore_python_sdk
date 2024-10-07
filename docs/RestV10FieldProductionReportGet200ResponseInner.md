# RestV10FieldProductionReportGet200ResponseInner

Field Production Report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_code_id** | **int** | ID of associated cost code | [optional] 
**cost_code** | **str** | Code and description of associated cost code | [optional] 
**budgeted_hours** | **float** | Number of labor hours budgeted for the given cost code | [optional] 
**actual_hours** | **float** | Number of labor hours logged for the given cost code to date | [optional] 
**remaining_hours** | **float** | Budgeted Hours - Actual Hours | [optional] 
**hours_utilization** | **str** | (Actual Hours / Budgeted Hours) * 100 | [optional] 
**projected_hours_at_completion** | **float** | (Actual Hours / Actual Quantities) * Remaining Quantities | [optional] 
**earned_hours** | **float** | (Budgeted Hours * Actual Quantities) / Budgeted Quantities | [optional] 
**budgeted_quantity** | **float** | Budgeted amount of a unit to install for the given cost code | [optional] 
**actual_quantity** | **float** | Actual amount of a unit installed for the given cost code to date | [optional] 
**remaining_quantities** | **float** | Budgeted Quantity - Actual Quantity | [optional] 
**unit_of_measure** | **str** | One of the following (ea, ls, lf, sf, sy, cy, mm, m, m^2, m^3, lbs, t, kg, ton) | [optional] 
**percent_complete** | **str** | (Actual Quantity / Budgeted Quantity) * 100 | [optional] 
**budgeted_production_rate** | **float** | Budgeted Quantity / Budgeted Hours | [optional] 
**actual_production_rate** | **float** | Actual Quantity / Actual Hours | [optional] 
**production_rate_variance** | **float** | Actual Production Rate - Budgeted Production Rate | [optional] 
**is_budgeted** | **str** | Cost code budgeted (yes/no) | [optional] 
**sub_job_name** | **str** | Name of the associated sub job | [optional] 
**sub_job_id** | **int** | ID of the associated sub job | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_field_production_report_get200_response_inner import RestV10FieldProductionReportGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FieldProductionReportGet200ResponseInner from a JSON string
rest_v10_field_production_report_get200_response_inner_instance = RestV10FieldProductionReportGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10FieldProductionReportGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_field_production_report_get200_response_inner_dict = rest_v10_field_production_report_get200_response_inner_instance.to_dict()
# create an instance of RestV10FieldProductionReportGet200ResponseInner from a dict
rest_v10_field_production_report_get200_response_inner_from_dict = RestV10FieldProductionReportGet200ResponseInner.from_dict(rest_v10_field_production_report_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


