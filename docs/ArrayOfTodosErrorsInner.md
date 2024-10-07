# ArrayOfTodosErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ToDo id | [optional] 
**assignment** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**color** | **str** | ToDo color | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**description** | **str** | ToDo description | [optional] 
**finish_datetime** | **datetime** | ToDo finish date-time | [optional] 
**full_outline_path** | **str** | ToDo full outline path (corresponds to matching field on Tasks) | [optional] 
**milestone** | **bool** | ToDo milestone status | [optional] 
**name** | **str** | ToDo name | [optional] 
**percentage** | **int** | ToDo percentage | [optional] 
**private** | **bool** | ToDo private status | [optional] 
**start_datetime** | **datetime** | ToDo start date-time | [optional] 
**task_name** | **str** | ToDo name (corresponds to matching field on Tasks) | [optional] 
**updated_at** | **datetime** | Date/time the ToDo was last updated | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_todos_errors_inner import ArrayOfTodosErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTodosErrorsInner from a JSON string
array_of_todos_errors_inner_instance = ArrayOfTodosErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfTodosErrorsInner.to_json())

# convert the object into a dict
array_of_todos_errors_inner_dict = array_of_todos_errors_inner_instance.to_dict()
# create an instance of ArrayOfTodosErrorsInner from a dict
array_of_todos_errors_inner_from_dict = ArrayOfTodosErrorsInner.from_dict(array_of_todos_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


