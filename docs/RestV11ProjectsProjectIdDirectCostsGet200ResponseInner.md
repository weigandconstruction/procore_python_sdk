# RestV11ProjectsProjectIdDirectCostsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**amount** | **str** | Grand total | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**direct_cost_type** | **str** | Type | [optional] 
**direct_cost_date** | **date** | Date | [optional] 
**grand_total** | **str** | Grand total | [optional] 
**invoice_number** | **str** | Unique identifier for a Direct Cost Item of type invoice | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**payment_date** | **date** | Payment Date | [optional] 
**received_date** | **date** | Received Date | [optional] 
**status** | **str** | Status | [optional] 
**terms** | **str** | The agreed upon Terms for the date of payment | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor** | **str** | Vendor name | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**vendor_name** | **str** | Vendor name | [optional] 
**currency_configuration** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration**](RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration.md) |  | [optional] 
**employee** | [**RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee**](RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_get200_response_inner import RestV11ProjectsProjectIdDirectCostsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdDirectCostsGet200ResponseInner from a JSON string
rest_v11_projects_project_id_direct_costs_get200_response_inner_instance = RestV11ProjectsProjectIdDirectCostsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdDirectCostsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_direct_costs_get200_response_inner_dict = rest_v11_projects_project_id_direct_costs_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdDirectCostsGet200ResponseInner from a dict
rest_v11_projects_project_id_direct_costs_get200_response_inner_from_dict = RestV11ProjectsProjectIdDirectCostsGet200ResponseInner.from_dict(rest_v11_projects_project_id_direct_costs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


