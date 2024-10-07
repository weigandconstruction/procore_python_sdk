# RestV10ProjectsProjectIdDirectCostsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**attachments_count** | **int** | Attachments count | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**direct_cost_type** | **str** | Type | [optional] 
**employee** | [**RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee**](RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee.md) |  | [optional] 
**invoice_number** | **str** | Unique identifier for a Direct Cost Item of type invoice | [optional] 
**direct_cost_date** | **date** | Date | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**grand_total** | **str** | Grand total | [optional] 
**line_items_count** | **int** | Line Items count | [optional] 
**payment_date** | **date** | Payment Date | [optional] 
**received_date** | **date** | Received Date | [optional] 
**status** | **str** | Status | [optional] 
**terms** | **str** | The agreed upon Terms for the date of payment | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor** | [**RestV11ProjectsProjectIdDirectCostsPost201ResponseVendor**](RestV11ProjectsProjectIdDirectCostsPost201ResponseVendor.md) |  | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**vendor_name** | **str** | Vendor name | [optional] 
**currency_configuration** | [**RestV10PaymentApplicationsIdGet200ResponseAllOfG703InnerCurrencyConfiguration**](RestV10PaymentApplicationsIdGet200ResponseAllOfG703InnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_post201_response import RestV10ProjectsProjectIdDirectCostsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDirectCostsPost201Response from a JSON string
rest_v10_projects_project_id_direct_costs_post201_response_instance = RestV10ProjectsProjectIdDirectCostsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDirectCostsPost201Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_direct_costs_post201_response_dict = rest_v10_projects_project_id_direct_costs_post201_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDirectCostsPost201Response from a dict
rest_v10_projects_project_id_direct_costs_post201_response_from_dict = RestV10ProjectsProjectIdDirectCostsPost201Response.from_dict(rest_v10_projects_project_id_direct_costs_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


