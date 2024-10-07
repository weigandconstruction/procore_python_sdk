# RestV10CoordinationIssuesGet200ResponseInnerAllOfAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 
**viewable** | **bool** | Boolean value indicating whether or not a viewable document has been created for the file. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_attachments_inner import RestV10CoordinationIssuesGet200ResponseInnerAllOfAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfAttachmentsInner from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_attachments_inner_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfAttachmentsInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_attachments_inner_dict = rest_v10_coordination_issues_get200_response_inner_all_of_attachments_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfAttachmentsInner from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_attachments_inner_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfAttachmentsInner.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


