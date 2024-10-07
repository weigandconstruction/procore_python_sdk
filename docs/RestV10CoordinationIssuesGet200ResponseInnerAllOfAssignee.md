# RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee

Login Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Login Information ID | [optional] 
**name** | **str** | User name | [optional] 
**login** | **str** | User email | [optional] 
**company_name** | **str** | User Company name. If the user belongs to a vendor, the vendor name will be returned. | [optional] 
**locale** | **str** | User dictionary | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_assignee import RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_assignee_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_assignee_dict = rest_v10_coordination_issues_get200_response_inner_all_of_assignee_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_assignee_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


