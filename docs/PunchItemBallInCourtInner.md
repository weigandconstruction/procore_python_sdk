# PunchItemBallInCourtInner

Login Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Login Information ID | [optional] 
**name** | **str** | User name | [optional] 
**locale** | **str** | User dictionary | [optional] 

## Example

```python
from procore_sdk.models.punch_item_ball_in_court_inner import PunchItemBallInCourtInner

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemBallInCourtInner from a JSON string
punch_item_ball_in_court_inner_instance = PunchItemBallInCourtInner.from_json(json)
# print the JSON string representation of the object
print(PunchItemBallInCourtInner.to_json())

# convert the object into a dict
punch_item_ball_in_court_inner_dict = punch_item_ball_in_court_inner_instance.to_dict()
# create an instance of PunchItemBallInCourtInner from a dict
punch_item_ball_in_court_inner_from_dict = PunchItemBallInCourtInner.from_dict(punch_item_ball_in_court_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


