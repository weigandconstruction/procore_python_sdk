# RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner

Actual Production Quantity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**unit_of_measure** | **str** | The unit of measure the Actual Production Quantity was created with | [optional] 
**quantity** | **float** | Amount of cost code installed | [optional] 
**timesheet_id** | **int** | The Timesheet ID the Actual Production Quantity was created with | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**crew** | [**TimecardEntry8Crew**](TimecardEntry8Crew.md) |  | [optional] 
**sub_job** | [**RestV10SubJobsGet200ResponseInner**](RestV10SubJobsGet200ResponseInner.md) |  | [optional] 
**updated_at** | **datetime** | Date the actual production quantity was updated | [optional] 
**created_at** | **datetime** | Date the actual production quantity was created | [optional] 
**cost_code** | [**RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode**](RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode.md) |  | [optional] 
**deleted_at** | **datetime** | Date the actual production quantity was deleted | [optional] 
**created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**var_date** | **date** | Date the actual production quantity was installed (YYYY-MM-DD) | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_get200_response_inner import RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_actual_production_quantities_get200_response_inner_instance = RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_actual_production_quantities_get200_response_inner_dict = rest_v10_projects_project_id_actual_production_quantities_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner from a dict
rest_v10_projects_project_id_actual_production_quantities_get200_response_inner_from_dict = RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.from_dict(rest_v10_projects_project_id_actual_production_quantities_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


