# RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Party Person ID | [optional] 
**first_name** | **str** | First name of the Party Person | [optional] 
**last_name** | **str** | Last name of the Party Person | [optional] 
**name** | **str** | Full name of the Party Person | [optional] 
**vendor** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManagerVendor**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManagerVendor.md) |  | [optional] 
**user_id** | **int** | Login Information ID associated with the Party Person | [optional] 
**is_employee** | **bool** | Indicates whether Party is an Employee of the current Company | [optional] 
**employee_id** | **str** | Employee ID of the Party | [optional] 
**potential_approver** | **bool** | Flag denoting if Party Person can act as Action Plan Approver | [optional] 
**potential_assignee** | **bool** | Flag denoting if Party Person can act as Action Plan Item Assignee | [optional] 
**potential_manager** | **bool** | Flag denoting if Party Person can act as Action Plan Manager | [optional] 
**potential_receiver** | **bool** | Flag denoting if Party Person can act as Action Plan Receiver | [optional] 
**updated_at** | **datetime** | Time the Party Person was updated | [optional] 
**login** | **str** | Login of the Party Person | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_parties_get200_response_inner import RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_parties_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_parties_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_parties_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_parties_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_parties_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


