# RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner

Invoice Change History

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**column** | **str** | Name of the column changed | [optional] 
**old_value** | **str** | Value of the column before change | [optional] 
**new_value** | **str** | Value of the column after change | [optional] 
**action_by** | **str** | Name of the person who made the change | [optional] 
**action_by_id** | **int** | ID of the person who made the change | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**ref_id** | **int** | The reference ID for the change | [optional] 
**ref_type** | **str** | The rereference type for the change | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_requisitions_requisition_id_change_histories_get200_response_inner import RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner from a JSON string
rest_v10_requisitions_requisition_id_change_histories_get200_response_inner_instance = RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_requisitions_requisition_id_change_histories_get200_response_inner_dict = rest_v10_requisitions_requisition_id_change_histories_get200_response_inner_instance.to_dict()
# create an instance of RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner from a dict
rest_v10_requisitions_requisition_id_change_histories_get200_response_inner_from_dict = RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner.from_dict(rest_v10_requisitions_requisition_id_change_histories_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


