# Body104CoordinationIssueViewpointsInnerVisibility

Object visibility settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_visibility** | **bool** |  | [optional] 
**exceptions** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body104_coordination_issue_viewpoints_inner_visibility import Body104CoordinationIssueViewpointsInnerVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of Body104CoordinationIssueViewpointsInnerVisibility from a JSON string
body104_coordination_issue_viewpoints_inner_visibility_instance = Body104CoordinationIssueViewpointsInnerVisibility.from_json(json)
# print the JSON string representation of the object
print(Body104CoordinationIssueViewpointsInnerVisibility.to_json())

# convert the object into a dict
body104_coordination_issue_viewpoints_inner_visibility_dict = body104_coordination_issue_viewpoints_inner_visibility_instance.to_dict()
# create an instance of Body104CoordinationIssueViewpointsInnerVisibility from a dict
body104_coordination_issue_viewpoints_inner_visibility_from_dict = Body104CoordinationIssueViewpointsInnerVisibility.from_dict(body104_coordination_issue_viewpoints_inner_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


