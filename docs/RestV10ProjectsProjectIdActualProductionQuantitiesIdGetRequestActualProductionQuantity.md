# RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequestActualProductionQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Amount installed | 
**crew_id** | **int** | The ID of the crew for the Actual Production Quantity | [optional] 
**location_id** | **int** | The Location ID for the Actual Production Quantity | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_id_get_request_actual_production_quantity import RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequestActualProductionQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequestActualProductionQuantity from a JSON string
rest_v10_projects_project_id_actual_production_quantities_id_get_request_actual_production_quantity_instance = RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequestActualProductionQuantity.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequestActualProductionQuantity.to_json())

# convert the object into a dict
rest_v10_projects_project_id_actual_production_quantities_id_get_request_actual_production_quantity_dict = rest_v10_projects_project_id_actual_production_quantities_id_get_request_actual_production_quantity_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequestActualProductionQuantity from a dict
rest_v10_projects_project_id_actual_production_quantities_id_get_request_actual_production_quantity_from_dict = RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequestActualProductionQuantity.from_dict(rest_v10_projects_project_id_actual_production_quantities_id_get_request_actual_production_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


