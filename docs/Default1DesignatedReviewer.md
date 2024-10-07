# Default1DesignatedReviewer

Prime CO Designated Reviewer. This field is only supported for single-tier projects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.default1_designated_reviewer import Default1DesignatedReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of Default1DesignatedReviewer from a JSON string
default1_designated_reviewer_instance = Default1DesignatedReviewer.from_json(json)
# print the JSON string representation of the object
print(Default1DesignatedReviewer.to_json())

# convert the object into a dict
default1_designated_reviewer_dict = default1_designated_reviewer_instance.to_dict()
# create an instance of Default1DesignatedReviewer from a dict
default1_designated_reviewer_from_dict = Default1DesignatedReviewer.from_dict(default1_designated_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


