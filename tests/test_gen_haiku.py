import pytest
from unittest.mock import MagicMock
from src.gen_haiku import gen_haiku

def test_gen_haiku_俳句にひらがな以外が含まれていた場合(mocker):

    # Given: モックの用意
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="とうきょうの ひかりさします タワーかな"))] # ひらがな以外が含まれるためエラーになるはず
    )
    mocker.patch("src.gen_haiku.OpenAI", return_value=mock_client)

    # When: gen_haiku()の実行
    with pytest.raises(ValueError) as e:
        gen_haiku("東京タワー")

    # Then: 結果の確認
    assert "生成された俳句にひらがな以外の文字が含まれています" in str(e.value)