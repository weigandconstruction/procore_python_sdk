# RestV10ChangeOrderPackagesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by_id** | **int** | Created by id | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Due date | [optional] 
**executed** | **bool** | Executed | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**signed_change_order_received_date** | **date** | Signed change order received date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**revision** | **int** | Revision | [optional] 
**grand_total** | **str** | Total including markup | [optional] 
**designated_reviewer** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_packages_get200_response_inner import RestV10ChangeOrderPackagesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderPackagesGet200ResponseInner from a JSON string
rest_v10_change_order_packages_get200_response_inner_instance = RestV10ChangeOrderPackagesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderPackagesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_change_order_packages_get200_response_inner_dict = rest_v10_change_order_packages_get200_response_inner_instance.to_dict()
# create an instance of RestV10ChangeOrderPackagesGet200ResponseInner from a dict
rest_v10_change_order_packages_get200_response_inner_from_dict = RestV10ChangeOrderPackagesGet200ResponseInner.from_dict(rest_v10_change_order_packages_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


